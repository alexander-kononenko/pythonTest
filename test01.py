import requests as re

print 'Count users which contains 5 in zipcode'
try:
    response = re.get('http://jsonplaceholder.typicode.com/users', timeout=(1000, 1))
    userTable = response.json()
    yes = 0
    no = 0
    for itemUsr in userTable:
        if '5' in str([itemUsr['address']['zipcode']]):
            yes += 1

        else:
            no += 1

    print "Number 5 is found for", yes, "users"
    print "For", no, "number 5 is not found"

    print "//////////////////////////"
    print "list with POST from body for used with id=3"

    responsePost = re.get('http://jsonplaceholder.typicode.com/posts', timeout=(1000, 1))
    postTable = responsePost.json()
    listPost = []
    for itemPst in postTable:
        if itemPst['userId'] == 3:
            listPost.append([itemPst['body']])
    print listPost

    # assert used 1 has todos

    responseTodos = re.get('http://jsonplaceholder.typicode.com/todos', timeout=(1000, 1))
    todosTable = responseTodos.json()
    q = 0
    for itemTodos in todosTable:
        if itemTodos['userId'] == 1:
            q += 1
    print "shtyk", q
    assert (q > 0), 'Not passed'


   

except re.exceptions.ReadTimeout:
    print('Oops. Read timeout occured')
except re.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')
