# Taken from https://github.com/hardikvasa/google-images-download

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"Keywords":"Empanadas", "limit":100, "print_urls":False}

absolute_images_paths = response.download(arguments)
