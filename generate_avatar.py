from avatar_generator import AvavatrGenerator

def generate_avatar():
    generator = AvavatrGenerator("./salim")
    generator.generate_avatar(1)
    
if __name__ == "__main__":
    generate_avatar()