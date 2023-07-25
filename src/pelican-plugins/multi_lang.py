from pelican import signals

def generate_multi_lang(generator):
    # make available in context

    generator.mlangs = [{'idioma':'español'},{'idioma':'english'}]
    generator._update_context(['mlangs'])

def register():
    signals.article_generator_finalized.connect(generate_multi_lang)

        # {{mlangs}}

        # {%for lang in mlangs%}
        #     <p> b {{lang.idioma}}</p>
        # {%endfor%}
