favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# language = favorite_language['sarah'].title()
# print(f"Sarah's favorite language is {language}")

# favorite_language['john'] = 'typescript'
# print(favorite_language)

print(f"favorite_language = {favorite_language}\n")


print("___Looping through key-value pairs___")
for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print("\n___Looping through all keys___")
friends = ['phil', 'sarah']
for name in favorite_language.keys():
    # Looping through keys is the default behavior
    # could also be written as "for name in favorite_language:"
    print(f"Hi {name.title()}")
    
    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        
if 'erin' not in favorite_language.keys():
    print("\nErin, please take our poll!")
    
print("\n___Looping through keys in a particular order___")
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\n___Looping through all values___")
print("The following languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())
    
print("\n___Looping through all values without repetition___")
for language in set(favorite_language.values()):
    print(language.title())