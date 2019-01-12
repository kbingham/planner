
FLASK = FLASK_APP=planner.py python3 -m flask

run:
	$(DEBUG) $(FLASK) run &
	xdg-open http://127.0.0.1:5000/


debug: run
