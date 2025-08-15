import pathlib
from zlib import crc32

def getXorKey(yuris_exe:pathlib.Path):
    # The starter in ascii is: "•W€–¾’©\x00\x00\x00\x00pac\x00"
    # Afterwords it's always followed by a title/creator's input name
    magic = b"\x95\x57\x8F\x80\x96\xBE\x92\xA9\x00\x00\x00\x00\x70\x61\x63\x00"
    block = yuris_exe.read_bytes()
    starterIdx = block.find(magic)
    if starterIdx <= 0:
        print("Cannot find Magic Starter String. Is this a Yu-Ris Game?")
        return
    end = block.find(b"YU-RIS Debug Info",starterIdx+len(magic))
    authorShip = block[starterIdx+len(magic):end].rstrip(b"\x00")
    print(f"authorShip is: \"{authorShip.decode('shift_jis')}\" | XOR int Key is: {hex(crc32(authorShip))}")
    

if __name__ == "__main__":
    import typer
    
    app = typer.Typer()
    
    @app.command()
    def main(yuris_bin:pathlib.Path):
        return getXorKey(yuris_bin)
    app()