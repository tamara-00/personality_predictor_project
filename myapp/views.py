from django.shortcuts import render
from .forms import SurveyForm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Загрување на LLM модел (мал)
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

def survey_view(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data["description"]

            # Подготовка на prompt
            prompt = f"""
            Classify the person as Introvert or Extrovert based on the following text.
            Answer only 'Introvert' or 'Extrovert', followed by a short reason.

            Example 1:
            Text: I enjoy spending most of my free time alone, reading or watching movies. Social events drain me.
            Personality: Introvert
            Reason: Prefers solitude and feels drained by social gatherings.

            Example 2:
            Text: I love going to parties and meeting new people. I feel energized when socializing.
            Personality: Extrovert
            Reason: Energized by social events and enjoys being with many friends.

            Example 3:
            Text: I like small gatherings with close friends, but I avoid large crowds.
            Personality: Introvert
            Reason: Selective about social interactions, prefers smaller groups.

            Example 4:
            Text: I often organize social events and meet friends almost every day.
            Personality: Extrovert
            Reason: Thrives on frequent social interactions.

            Now classify this person:
            Text:
            {user_text}
            """

            # Генерирање на предвидување
            inputs = tokenizer(prompt, return_tensors="pt")
            outputs = model.generate(**inputs, max_new_tokens=100, do_sample=True, top_k=50, top_p=0.95)
            prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)

            return render(request, "result.html", {"result": prediction})

    else:
        form = SurveyForm()

    return render(request, "survey.html", {"form": form})
