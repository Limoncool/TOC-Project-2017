import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '230188989:AAFgZtkRQJb_Ba_SPgi2rDhLXGrGp-0YgHg'
WEBHOOK_URL = 'https://86e84d0a.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
	'initial',
        'Beach',
        'Forest',
	'Town',
	'Mountain',
	'Underground',
	'Sinkship',
	'Undersea',
	'Lake',
	'Plain',
	'Market',
	'Trainstation',
	'Tower',
	'Spring',
	'Top',
	'Tomb',
	'Palace',

	'SinkshipY',
	'SinkshipN',
	'UnderseaY',
	'UnderseaN',
	'LakeY',
	'LakeN',
	'PlainY',
	'PlainN',
	'MarketY',
	'MarketN',
	'TrainstationY',
	'TrainstationN',
	'TowerY',
	'TowerN',
	'SpringY',
	'SpringN',
	'TopY',
	'TopN',
	'TombY',
	'TombN',
	'PalaceY',
	'PalaceN',
    ],
    transitions=[
	{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'initial',
            'conditions': 'Going_init'
        },
#=============first stage=============================
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'Beach',
            'conditions': 'Going_Beach'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'Forest',
            'conditions': 'Going_Forest'
        },
	{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'Town',
            'conditions': 'Going_Town'
        },
	{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'Mountain',
            'conditions': 'Going_Mountain'
        },
	{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'Underground',
            'conditions': 'Going_Underground'
        },
#=============second stage============================
#=======beach========
	{
            'trigger': 'advance',
            'source': 'Beach',
            'dest': 'Sinkship',
            'conditions': 'Going_Sinkship'
        },
        {
            'trigger': 'advance',
            'source': 'Beach',
            'dest': 'Undersea',
            'conditions': 'Going_Undersea'
        },
#=======forest=======
	{
            'trigger': 'advance',
            'source': 'Forest',
            'dest': 'Lake',
            'conditions': 'Going_Lake'
        },
	{
            'trigger': 'advance',
            'source': 'Forest',
            'dest': 'Plain',
            'conditions': 'Going_Plain'
        },
#=======town=========
	{
            'trigger': 'advance',
            'source': 'Town',
            'dest': 'Market',
            'conditions': 'Going_Market'
        },
	{
            'trigger': 'advance',
            'source': 'Town',
            'dest': 'Trainstation',
            'conditions': 'Going_Trainstation'
        },
	{
            'trigger': 'advance',
            'source': 'Town',
            'dest': 'Tower',
            'conditions': 'Going_Tower'
        },
#=======moutain======
	{
            'trigger': 'advance',
            'source': 'Mountain',
            'dest': 'Spring',
            'conditions': 'Going_Spring'
        },
	{
            'trigger': 'advance',
            'source': 'Mountain',
            'dest': 'Top',
            'conditions': 'Going_Top'
        },
#=======underground==
	{
            'trigger': 'advance',
            'source': 'Underground',
            'dest': 'Tomb',
            'conditions': 'Going_Tomb'
        },
	{
            'trigger': 'advance',
            'source': 'Underground',
            'dest': 'Palace',
            'conditions': 'Going_Palace'
        },
#=============third stage=============================
#=======beach========
	{
            'trigger': 'advance',
            'source': 'Sinkship',
            'dest': 'SinkshipY',
            'conditions': 'Sinkship_Yes'
        },
	{
            'trigger': 'advance',
            'source': 'Sinkship',
            'dest': 'SinkshipN',
            'conditions': 'Sinkship_No'
        },
        {
            'trigger': 'advance',
            'source': 'Undersea',
            'dest': 'UnderseaY',
            'conditions': 'Undersea_Yes'
        },
        {
            'trigger': 'advance',
            'source': 'Undersea',
            'dest': 'UnderseaN',
            'conditions': 'Undersea_No'
        },
#=======forest=======
	{
            'trigger': 'advance',
            'source': 'Lake',
            'dest': 'LakeY',
            'conditions': 'Lake_Yes'
        },
	{
            'trigger': 'advance',
            'source': 'Lake',
            'dest': 'LakeN',
            'conditions': 'Lake_No'
        },
	{
            'trigger': 'advance',
            'source': 'Plain',
            'dest': 'PlainY',
            'conditions': 'Plain_Yes'
        },
	{
            'trigger': 'advance',
            'source': 'Plain',
            'dest': 'PlainN',
            'conditions': 'Plain_No'
        },
#=======town=========
	{
            'trigger': 'advance',
            'source': 'Market',
            'dest': 'MarketY',
            'conditions': 'Market_Yes'
        },
	{
            'trigger': 'advance',
            'source': 'Market',
            'dest': 'MarketN',
            'conditions': 'Market_No'
        },
	{
            'trigger': 'advance',
            'source': 'Trainstation',
            'dest': 'TrainstationY',
            'conditions': 'Trainstation_Yes'
        },
	{
            'trigger': 'advance',
            'source': 'Trainstation',
            'dest': 'TrainstationN',
            'conditions': 'Trainstation_No'
        },
	{
            'trigger': 'advance',
            'source': 'Tower',
            'dest': 'TowerY',
            'conditions': 'Tower_Yes'
        },
	{
            'trigger': 'advance',
            'source': 'Tower',
            'dest': 'TowerN',
            'conditions': 'Tower_No'
        },
#=======moutain======
	{
            'trigger': 'advance',
            'source': 'Spring',
            'dest': 'SpringY',
            'conditions': 'Spring_Yes'
        },
	{
            'trigger': 'advance',
            'source': 'Spring',
            'dest': 'SpringN',
            'conditions': 'Spring_No'
        },
	{
            'trigger': 'advance',
            'source': 'Top',
            'dest': 'TopY',
            'conditions': 'Top_Yes'
        },
	{
            'trigger': 'advance',
            'source': 'Top',
            'dest': 'TopN',
            'conditions': 'Top_No'
        },
#=======underground==
	{
            'trigger': 'advance',
            'source': 'Tomb',
            'dest': 'TombY',
            'conditions': 'Tomb_Yes'
        },
	{
            'trigger': 'advance',
            'source': 'Tomb',
            'dest': 'TombN',
            'conditions': 'Tomb_No'
        },
	{
            'trigger': 'advance',
            'source': 'Palace',
            'dest': 'PalaceY',
            'conditions': 'Palace_Yes'
        },
	{
            'trigger': 'advance',
            'source': 'Palace',
            'dest': 'PalaceN',
            'conditions': 'Palace_No'
        },
#=============back stage==============================
        {
            'trigger': 'go_back',
            'source': [
                'initial',
		'SinkshipY',
		'SinkshipN',
		'UnderseaY',
		'UnderseaN',
		'LakeY',
		'LakeN',
		'PlainY',
		'PlainN',
		'MarketY',
		'MarketN',
		'TrainstationY',
		'TrainstationN',
		'TowerY',
		'TowerN',
		'SpringY',
		'SpringN',
		'TopY',
		'TopN',
		'TombY',
		'TombN',
		'PalaceY',
		'PalaceN',
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
