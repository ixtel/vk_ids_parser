import mechanize, os
print "Welcome to VK ID's PARSER"
print "Please enter group id which you want to scan"
group_id = raw_input ("")
br = mechanize.Browser()
br.open('https://api.vkontakte.ru/method/groups.getMembers?group_id='+group_id)
ids = br.response().read().split('"users":[')[1].split(']}}')[0]
ids = ids.split(',')
f = open('ids.txt', 'w')
for index in ids:
    f.write(index + '\n')
f.close()
print "Done"

