## Inject forms you know about

### Installation
Add this to your .bashrc (or .profile).
```
export SQLMAP_PATH="/path/to/gauntlt-demo/vendor/sqlmap/sqlmap.py"
```

### Challenge
See the challenge in `examples/form_injection/README.md`

You will need these switches for sqlmap, ` --batch --forms --dbms sqlite -p email,password`

### Solution
See `examples/form_injection/final_sqlmap-forms.attack`

