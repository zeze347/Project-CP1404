from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ProductEvent(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Initialise variables."""
        super().__init__(**kwargs)
        self.products = self.load_products("products.json")
        self.total = 0.0

    def build(self):
        """Create the interactive app."""
        self.title = "Shopping bill"
        self.root = Builder.load_file('shopping_app.kv')
        self.create_widgets()
        return self.root

    def product_button_pressed(self, button):
        """Add to total price."""
        self.root.ids.status_text.total += button.cost

    def create_widgets(self):
        """Create buttons from list of objects and add them to display."""
        self.status_text = f"Click on a product to buy it."
        for product in self.products:
            button = Button(str(product)) # Find Button reference (copied from Seminar demo)
            button.bind(on_release=self.press_entry)
            button.product = product
            self.root.ids.products_box.add_widget(button)

    def press_entry(self, instance):
        """Handle pressing product buttons."""
        product = instance.product
        self.total += product.price
        self.status_text = f"Total price ${self.total:,.2f}"

    def reset(self):
        """Reset the price."""
        self.total = 0.0
        self.status_text = f"Total price ${self.total:,.2f}"

    @staticmethod
    def load_products(filename):
        """Load products from a file."""
        with open(filename, "r", encoding="UTF8") as in_file:
            products = in_file.readlines()
        return products
