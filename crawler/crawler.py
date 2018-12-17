import csv
import gzip
import io
import json
import re
import requests
import shutil
from contextlib import closing


def get_tag_content(tag_name, text):
    return [n.group(1) for n in 
        re.finditer('%s(.+?)%s' % (('<%s>' % tag_name), 
                                   ('</%s>' % tag_name)),
                    text)]

def get_tag_property(property_name, tag_name, text):
	properties = re.search('<%s (.+?)>' % tag_name, text).group(1)
	if properties:
		for marker_property in properties.split():
			match = re.search('%s=(.*)' % property_name,  marker_property)
			if match:
				return match.group(1)
	return None

def collect_movie_files():
    r = requests.get("https://datasets.imdbws.com/")
    dataset_page_response_text = r.text
    movie_files_links = get_tag_content('ul', dataset_page_response_text)

    for movie_file_link in movie_files_links:
		file_link = get_tag_property('href', 'a', movie_file_link)
		file_get_request = requests.get(file_link)
		with closing(file_get_request), gzip.GzipFile(fileobj=io.BytesIO(file_get_request.content), mode='r') as archive, open('content_file.tsv', 'wb') as content_file:
			shutil.copyfileobj(archive, content_file)
		
		print "Processed %s" % file_link
		content_file.close()

		content_file = open('content_file.tsv', 'r')
		counter = 0
		if 'title.basics' in file_link:
			movies = {}
			with open('movies.json', 'w') as movies_json:
				content_lines = content_file.readlines()
				for line_number in range(len(content_lines)-1, len(content_lines) - 5001, -1):
					movie_infos = content_lines[line_number].split('\t')
					movies[movie_infos[0]] = movie_infos[1:]
					
					if counter >= 5000:
						break
					counter += 1
				json.dump(movies, movies_json)
			content_file.close()
		elif 'name.basics' in file_link:
			names = {}
			with open('names.json', 'w') as names_json:
				for line in content_file.readlines():
					name_infos = line.split('\t')
					names[name_infos[0]] = name_infos[1:]
				json.dump(names, names_json)
			content_file.close()


if __name__ == '__main__':
    collect_movie_files()