import mechanize, os
print "Welcome to VK ID's PARSER"
print "Please enter group id which you want to scan"
group_id = raw_input ("")
k2 = 0
offset = '0'
count = '0'
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_robots(False)
br.open('https://api.vk.com/method/groups.getMembers?group_id='+group_id+'&offset='+offset+'&count='+count)
count = br.response().read().split('{"response":{"count":')[1].split(',')[0]
k = count
k = float(k)
f = open('ids.txt', 'w')
while k > k2:
    br = mechanize.Browser()
    br.open('https://api.vk.com/method/groups.getMembers?group_id='+group_id+'&offset='+offset+'&count='+count)
    ids = br.response().read().split('"users":[')[1].split(']}}')[0]
    ids = ids.split(',')
    for index in ids:
        f.write(index + '\n')
    k2 = k2 + 1000
    offset = float(offset)
    offset = k2
    offset = str(offset)
    print (offset+'/'+count)
f.close()
print "Done"

