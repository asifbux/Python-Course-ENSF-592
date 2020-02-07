# MusicRoom module with Instruments
class MusicRoom:
    """Holding a list of instrument objects.

    Atrributes:
        instruments: List holding Instrument class objects.
    """

    def __init__(self, instruments):
        self.instruments = instruments

    def play(self, song):
        """Plays song on all instruments.

        song: string
        """

        # TODO: Add your code here
        for instruments in self.instruments:
            if type(instruments) != Drums and instruments.play(song):
                Instrument.play(instruments, song)
            else:
                Instrument.play(instruments, song)

    def tune(self):
        """Tunes all instruments that are not currently tuned."""

        #TODO: Add your code here
        for instrument in self.instruments:
            if (type(instrument) != Drums and (instrument.play_count > type(instrument).detune_count)):
                instrument.is_tuned = True
                instrument.play_count = 0
                print('    ', instrument)

class Instrument:
    """Parent class for instruments

    Atrributes:
        kind: string describing the type of instrument
        brand: string instrument maker/brand
        year: string year instrument was made
        is_tuned: bool, True if currently tuned, False otherwise
    """

    kind = 'Instrument'

    def __init__(self, brand, year, is_tuned=True):
        # TODO: Add your code here
        self.brand = brand
        self.year = year
        self.is_tuned = True

    def __str__(self):
        """Human readable representation of the instrument."""
        # TODO: Add your code here
        return str('Tuning a {} {} {}'.format(self.year, self.brand, self.kind))

    def play(self, song):
        """plays song on instrument.

        Song will 'sound' different if instrument is not tuned.

        song: string

        returns: string representing song played
        """
        # TODO: Add your code here
        if (self.is_tuned):
            print('{} plays: {}'.format(self.kind, song))
        else:
            print('{} plays: {}'.format(self.kind, str(song).swapcase()))


class Guitar(Instrument):
    """ A Guitar extends Instrument

    Instrument kind is 'Guitar'

    de-tunes after playing a song.
    """

    kind = 'Guitar'
    detune_count = 1

    def __init__(self, brand, year):
        super().__init__(brand, year)
        self.play_count = 0

    def play(self, song):
        """plays song and de-tunes.

        song: string
        returns: string representing song played
        """
        # TODO: Add your code here
        if (self.play_count < Guitar.detune_count):
            self.play_count += 1
            return True
        else:
            self.play_count += 1
            self.is_tuned = False
            return False


class Bass(Instrument):
    """ A Bass extends Instrument

    Instrument kind is 'Bass'

    de-tunes after playing two songs.

    Atrributes:
        detune_count: integer how many songs until de-tuned (default is 2)
        play_count: integer how many songs played
    """

    kind = 'Bass'
    detune_count = 2

    def __init__(self, brand, year):
        super().__init__(brand, year)
        self.play_count = 0

    def play(self, song):
        """plays song and de-tunes if played detune_count songs.

        song: string
        returns: string representing song played
        """
        # TODO: Add your code here
        if (self.play_count < Bass.detune_count):
            self.play_count += 1
            return True
        else:
            self.play_count += 1
            self.is_tuned = False
            return False


class Drums(Instrument):
    """ Drums extends Instrument

    Instrument kind is 'Drums'

    Never de-tunes.
    """

    kind = 'Drums'

    def play(self, song):
        """plays song like Instrument.

        song: string
        returns: string representing song played
        """
        res = super().play(song)
        return res


if __name__ == '__main__':
    # Create instances of Instruments
    my_instruments = [
        Bass("Ibanez", '2001'),
        Guitar("Fender", '1998'),
        Drums("Pearl", '2010')
    ]

    # Instantiate the MusicRoom class
    my_music_room = MusicRoom(my_instruments)

    # Rehearsing
    for i in range(3):
        my_music_room.play('Metallica - Nothing Else Matters')
        print('\n')

    # Tune instruments
    my_music_room.tune()

    print("Done tuning\n")

    # Concert
    my_music_room.play('Metallica - Nothing Else Matters')

    ''' More test cases below'''
    # for i in range(3):
    #     my_music_room.play('Metallica - Nothing Else Matters')
    #     print('\n')
    #
    # my_music_room.tune()
    #
    # my_music_room.play('Metallica - Nothing Else Matters')
