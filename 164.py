url = 'https://post.naver.com/viewer/postView.naver?volumeNo=32490410&memberNo=15460571'

tmp = url.split('?')
queries = tmp[1].split('&')
for query in queries:
    print(query)
