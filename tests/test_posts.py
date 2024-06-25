

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    print('===============================')
    # print(res.)
    # assert len(res.json())==len(test_posts)
    assert res.status_code == 200