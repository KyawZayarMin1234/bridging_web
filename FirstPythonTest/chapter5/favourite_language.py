favourite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favourite_language['sarah'].title()
print(f"Sarah's favourite language is {language}")

# accessing value with [] and geet()
language2 = favourite_language.get('je','person does not exist.')
print(language2.title())