install:
	@pip install -e .

clean_terminal:
	@clear


github:
	@git add . & git commit -m "push" & git push origin master
