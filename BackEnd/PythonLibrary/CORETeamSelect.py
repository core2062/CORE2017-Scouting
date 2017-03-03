#!/usr/bin/python
# Allow Display of elements in HTML

import COREDependencies

print("Content-type:text/html\r\n\r\n")
print('<html class="no-js" lang="en">')
print('<head>')
print('<meta charset="utf-8">')
print('<link rel="shortcut icon" href="favicon.ico" />')
print('<meta name="description" content="CORE 2062 Scouting">')
print('<meta name="author" content="CORE2062">')
print('<meta name="robots" content="noindex, nofollow">')
print('<meta name="theme-color" content="#ff731c" />')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">')
print('<title>CORE 2062 Scouting | Match Display</title>')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css" ' +
      'integrity="sha256-t2/7smZfgrST4FS1DT0bs/KotCM74XlcqZN5Vu7xlrw=" crossorigin="anonymous" />')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css" ' +
      'integrity="sha256-NTds7atVCDeolLUzbcl45lx4gJYO+hNXCaX1wC2HQHc=" crossorigin="anonymous" />')
print('<link rel="stylesheet" href="css/app.css">')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js" integrity="' +
      'sha256-0rguYS0qgS6L4qVzANq4kjxPLtvnp5nn2nB5G1lWRv4=" crossorigin="anonymous"></script>')
print('</head>')
print('<body>')

cellColorizer = COREDependencies.COREClassColor.ColorTeam()
print('<table width="100%">')
print('<thead>')
print('<tr>')
print('<th rowspan="2" width="20%">Match #</th>')
print('<th colspan="3" width="40%">Red Alliance</th>')
print('<th colspan="3" width="40%">Blue Alliance</th>')
print('</tr>')
print('<tr>')
for i in range(1, 7):
    if i <= 3:
        print('<th> Red Team #' + str(i) + '</th>')
    else:
        print('<th> Blue Team #' + str((i-3)) + '</th>')
print('</tr>')
print('</thead>')
match_num = 1
for match in COREDependencies.COREMatchSchedule.SCHEDULE:
    print('<tr>')
    print('<td>' + str(match_num) + '</td>')
    for team in match:
        if cellColorizer.submit_color(team, match_num)  == None:
            print('<td><a href ="prepopulate.php?team=' + str(team) + '&match=' + str(match_num) +
                  '">' + str(team) + ' </td>')
        else:
            print('<td class ="' + cellColorizer.submit_color(team, match_num) +
                  '">' + str(team) + ' </td>')
    print('</tr>')
    match_num += 1
print('</table>')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="' +
      'sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation.min.js" integrity=' +
      '"sha256-KXypdIy75PPHsbEaVkrhBvlQg8XTQy8NvalzrIxMrco=" crossorigin="anonymous"></script>')
print('<script>')
print('$(document).foundation();')
print('</script>')
print('</body>')
print('</html>')