class TextModifier:
    def __init__(self, text):
        self.text = text

    def uppercase(self):
        self.text = self.text.upper()

    def lowercase(self):
        self.text = self.text.lower()

    def remove_spaces(self):
        self.text = self.text.replace(" ", "")

    def encrypt(self, shift):
        encrypted_text = ""
        for char in self.text:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                encrypted_text += shifted_char
            else:
                encrypted_text += char
        self.text = encrypted_text

modifier = TextModifier("Hello, World!")

modifier.uppercase()
print("Uppercase:", modifier.text)

modifier.lowercase()
print("Lowercase:", modifier.text)

modifier.remove_spaces()
print("Without spaces:", modifier.text)

modifier.encrypt(3)
print("Encrypted:", modifier.text)