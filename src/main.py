from textnode import TextType,TextNode

def main():
    # Initialize the text node
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")

    # Display the text
    print(node)


if __name__ == "__main__":
    main()