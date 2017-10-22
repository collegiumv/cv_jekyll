import jinja2

contents = ''
with open('desc.txt') as desc:
    contents = desc.read()

entries = contents.split('\n\n\n')

for entry in entries:
    page = {}
    split = entry.split('\n\n')
    headers = [header.strip() for header in split[0].split('\t') if header]
    page['id'] = headers[0]
    page['name'] = headers[1]
    try:
        page['instructor'] = headers[2]
    except:
        pass
    page['desc'] = "\n\n".join(split[1:])
    filename = page['name'].lower().replace(' ', '-')
    filename = filename.replace('&', 'and')
    filename = filename.replace(',', '')
    filename = filename.replace('’', '')
    env = jinja2.Environment(loader=jinja2.loaders.FileSystemLoader("."))
    template = env.get_template("format.j2")
    with open('out/' + filename + ".md", 'w') as outfile:
        outfile.write(template.render(page) + '\n')
    print('  * [{}] ({}/)'.format(page['name'], filename))
