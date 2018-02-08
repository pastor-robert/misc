from bs4 import BeautifulSoup
# coding: utf-8

html_doc = '''
<td class='translation'>
    <span class='italiano'>ciao</span>
    <span class='french'>au revoir</span>
    <span class='polish'>cześć</span>
</td>
'''

soup = BeautifulSoup(html_doc)
t = soup.select("td.translation span.polish")[0].text
print type(t), t
print t.encode('utf-8')
