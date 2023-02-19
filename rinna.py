import torch
import re
from transformers import T5Tokenizer, AutoModelForCausalLM

tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt-1b")
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt-1b")

if torch.cuda.is_available():
    model = model.to("cuda")

def main():
    text='大学合格したよ！'
    print(generate_text(text))

def generate_text(input):
    token_ids = tokenizer.encode(input, add_special_tokens=False, return_tensors="pt")
    leng = len(input)

    with torch.no_grad():
        output_ids = model.generate(
            token_ids.to(model.device),
            max_length=leng+500,
            min_length=50,
            temperature=0.5,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.5,
            pad_token_id=tokenizer.pad_token_id,
            bos_token_id=tokenizer.bos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            #bad_word_ids=[[tokenizer.unk_token_id]]
        )

    output = tokenizer.decode(output_ids.tolist()[0])
    print(output + "\n")
    output2 = (output[leng:])

    pattern = r"AI:|私:|俺:|僕:|あなた:|相手:|<unk>|</s>|[UNK]"
    if re.search(pattern, output2) != None:
        match_position = [match.span() for match in re.finditer(pattern, output2)]
        first_match_position = match_position[0][0]
        edited_text = output2[:first_match_position]
        print("\n" + edited_text)
        return edited_text
    else:
        return output2


if __name__ == '__main__':
    main()