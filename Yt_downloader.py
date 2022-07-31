import webbrowser
url=input("Enter The Video URL: ")
url=url[:12]+'ss'+url[12:]
webbrowser.open(url)
