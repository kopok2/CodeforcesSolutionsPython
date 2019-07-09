try:
    result = True
    jabber_id = input().lower().replace("/n", "")
    username = jabber_id.split("@", 1)[0]
    hostname = jabber_id.split("@", 1)[1].split("/")[0]
    try:
        resource = jabber_id.split("@", 1)[1].split("/", 1)[1]
        if not resource:
            result = False
    except:
        resource = ""
    usp = 'abcdefghijklmnopqrstuvwxyz_1234567890'
    uhp = 'abcdefghijklmnopqrstuvwxyz_1234567890.'
    
    for c in username:
        if not c in usp:
            #print("1")
            result = False
    for c in hostname:
        if not c in uhp:
            #print("2")
            result = False
    for c in resource:
        if not c in usp:
            #print("3")
            result = False
    if not( len(username)<=16 and len(username)>0):
        #print("4")
        result = False
    if not( len(hostname)<=32 and len(hostname)>0):
        #print("5")
        result = False
    if not len(resource)<=16:
        #print("6")
        result = False
    #print(hostname.split("."))
    for h in hostname.split("."):
        if len(h)==0:
            #print("7")
            result = False
    if resource:
        for h in resource.split("/"):
            if len(h)==0:
                #print("8")
                result = False
    if result:
        print("YES")
    else:
        print("NO")
except:
    print("NO")
#print(username, " ", hostname, " ", resource)
