from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/get-aria', methods=['POST'])
def get_aria():
    data = request.json
    code = data.get('code', '')

    # OpenAI prompt
    prompt = f"""
    Analyze the following code (HTML, CSS, JS) and suggest ARIA attributes to improve accessibility. 
    Provide updated HTML code with ARIA attributes applied:
    {code}
    """

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7
        )
        suggestions = response['choices'][0]['text'].strip()
        return jsonify({'suggestions': suggestions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
