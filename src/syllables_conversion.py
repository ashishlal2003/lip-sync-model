import pyphen
import json
dic = pyphen.Pyphen(lang='en')

# Define words and phrases
words = {
    1: "Begin",
    2: "Choose",
    3: "Connection",
    4: "Navigation",
    5: "Next",
    6: "Previous",
    7: "Start",
    8: "Stop",
    9: "Hello",
    10: "Web"
}

phrases = {
    1: "Stop navigation.",
    2: "Excuse me.",
    3: "I am sorry.",
    4: "Thank you.",
    5: "Good bye.",
    6: "I love this game.",
    7: "Nice to meet you.",
    8: "You are welcome.",
    9: "How are you?",
    10: "Have a good time."
}

def break_into_syllables(text):
    words_in_text = text.split()
    syllables_list = []
    for word in words_in_text:
        syllables = dic.inserted(word.strip('.')) 
        syllables_list.append(syllables)
    return syllables_list

def map_syllables_to_frames(syllables, total_frames):
    frame_mapping = {}
    syllable_count = sum([len(s.split('-')) for s in syllables])
    frames_per_syllable = total_frames // syllable_count if syllable_count else 0  

    frame_index = 1
    for syllable_group in syllables:
        for syllable in syllable_group.split('-'):
            for _ in range(frames_per_syllable):
                frame_mapping[f"frame{frame_index}"] = syllable
                frame_index += 1
    return frame_mapping
total_instances = 3000
words_per_instance = 10
phrases_per_instance = 10
frame_rate_per_instance = 1
word_frame_count = total_instances // words_per_instance 
phrase_frame_count = total_instances // phrases_per_instance 

processed_words = []
for word_id, word_text in words.items():
    syllables = break_into_syllables(word_text)
    frame_mapping = map_syllables_to_frames(syllables, word_frame_count)
    processed_words.append({
        "id": word_id,
        "text": word_text,
        "syllables": syllables,
        "frame_to_syllable_mapping": frame_mapping
    })

# Process phrases
processed_phrases = []
for phrase_id, phrase_text in phrases.items():
    syllables = break_into_syllables(phrase_text)
    frame_mapping = map_syllables_to_frames(syllables, phrase_frame_count)
    processed_phrases.append({
        "id": phrase_id,
        "text": phrase_text,
        "syllables": syllables,
        "frame_to_syllable_mapping": frame_mapping
    })

# Save the processed data into a JSON file
data = {
    "processed_words": processed_words,
    "processed_phrases": processed_phrases
}

with open("assets/syllables_data.json", "w") as f:
    json.dump(data, f, indent=4)

# Output the processed data for words and phrases
print("Processed Words and Phrases data has been saved to syllables_data.json")
