import importlib
modules = ['streamlit','pandas','numpy','pickle','plotly','sklearn']
for m in modules:
    try:
        mod = importlib.import_module(m)
        v = getattr(mod, '__version__', 'builtin or no __version__')
        print(f'{m}: OK ({v})')
    except Exception as e:
        print(f'{m}: ERROR -> {type(e).__name__}: {e}')
