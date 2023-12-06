from flask import Flask, render_template, request, session, flash
from chatgpt import call_openai_api
from weather import main as get_weather
from datetime import timedelta

app = Flask(__name__, template_folder='index.html')
app.secret_key = 'your_secret_key'

app.permanent_session_lifetime = timedelta(seconds=60)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = session.get('weather_data', None)
    openai_data = session.get('openai_data', None)

    if request.method == 'POST':
        if 'get_weather' in request.form:
            city = request.form['cityName']
            state = request.form['stateName']
            country = request.form['countryName']

            
            if not city or not state or not country:
                flash('Please enter valid city, state, and country.')
            else:
                try:
                    weather_data = get_weather(city, state, country)
                    session['weather_data'] = weather_data
                except Exception as e:
                    flash(f'Error fetching weather data: {str(e)}')

        elif 'call_openai' in request.form:
            user_prompt = request.form['userPrompt']

            
            if not user_prompt:
                flash('Please enter a valid user prompt.')
            else:
                try:
                    openai_data = call_openai_api(user_prompt)
                    session['openai_data'] = openai_data
                except Exception as e:
                    flash(f'Error calling OpenAI API: {str(e)}')

    return render_template('index.html', weather_data=weather_data, openai_data=openai_data)

if __name__ == '__main__':
    app.run(debug=False)







