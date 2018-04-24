composer.py
    import sink
    import source
    import translator

sink = Sink(filename)
source = Source(network address)
translator = Translator()

translator.bind(source)
sink.bind(translator)
