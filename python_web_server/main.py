async def app(scope, receive, send):
    assert scope['type'] == 'http'

    try:
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                (b'content-type', b'text-plain'),
                # (b'content-length', b'100'),
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': b'<h1>Hello, world!</h1>',
        })
    except Exception as ex:
        print("failed to start server")
        print(f"Error", {ex})