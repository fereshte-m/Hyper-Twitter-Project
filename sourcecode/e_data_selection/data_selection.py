import sourcecode.d_data_analysis_visual.data_analysis_visual as vs

print("Welcome to our Twitter project for Python module!")
print("Below, you see the list of hashtags collected for this project. Please select one hashtag to see the relevant visual analysis:")


hashtag_list = ["HoseinRonaghi", "IranRevolution", "MahsaAmini", "MohsenShekari", "OpIran", "WomenLifeFreedom"]
for index, element in enumerate(hashtag_list):
    print(index, ":", element)

while True:
    hashtag = int(input("Enter the index of the hashtag: "))
    if 0 <= hashtag < len(hashtag_list):
        print("You have selected: ", hashtag_list[hashtag])
        break
    else:
        print("This index is not available in the list.")


while True:
    visual_analysis_word = input("Enter 'M' to see the most frequent words, and 'L' to see the least frequent words: ")
    if visual_analysis_word.upper() != 'M' and visual_analysis_word.upper() != 'L':
        print(f'{visual_analysis_word} not available')
    else:
        break

while True:
    visual_analysis_hashtag = input("Enter 'M' to see the most frequent hashtags, "
                                    "and 'L' to see the least frequent hashtags: ")
    if visual_analysis_hashtag.upper() != 'M' and visual_analysis_hashtag.upper() != 'L':
        print(f'{visual_analysis_hashtag} not available')
    else:
        break

while True:
    visual_analysis_mention = input("Enter 'M' to see the most frequent mentions,"
                                    "and 'L' to see the least frequent mentions: ")
    if visual_analysis_mention.upper() != 'M' and visual_analysis_mention.upper() != 'L':
        print(f'{visual_analysis_mention} not available')
    else:
        break


vs.plot_data(hashtag_list[hashtag],
             visual_analysis_word.upper(),
             visual_analysis_hashtag.upper(),
             visual_analysis_mention.upper())
