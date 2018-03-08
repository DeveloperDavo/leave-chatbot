# Leave Chatbot
Train the NLU model with `python -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current` <br/>
Train the dialog model with `python -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue` <br/>
Run server with `python -m rasa_core.server -d models/dialogue -u models/nlu/default/current` <br/>
Run CLI with `python -m rasa_core.run -d models/dialogue -u models/nlu/default/current` <br/>
