import tensorflow as tf # pragma: no cover
from keras import layers # pragma: no cover


## Removing from tests for now since I am not sure I'll keep using discriminatos and generator
class Discriminator(tf.keras.Model):  # pragma: no cover
    def __init__(self, input_dim, n_layers, n_units, dropout_rate):
        super(Discriminator, self).__init__()
        self.model = tf.keras.Sequential()
        self.model.add(layers.Dense(n_units, input_dim=input_dim))
        self.model.add(layers.LeakyReLU(alpha=0.2))
        self.model.add(layers.Dropout(dropout_rate))
        for _ in range(n_layers - 1):
            self.model.add(layers.Dense(n_units // 2))
            self.model.add(layers.LeakyReLU(alpha=0.2))
            self.model.add(layers.Dropout(dropout_rate))
        self.model.add(layers.Dense(1, activation="sigmoid"))

    def call(self, inputs):
        return self.model(inputs)


def build_discriminator(input_dim, n_layers, n_units, learning_rate, dropout_rate): # pragma: no cover
    discriminator = Discriminator(input_dim, n_layers, n_units, dropout_rate)
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    return discriminator, optimizer


## Below code only makes sense when running local so will not be considered for teste
if __name__ == "__main__":  # pragma: no cover
    # Exemplo de uso para verificar a arquitetura
    input_dim = 11  # Número de features nos seus dados
    n_layers_disc = 3
    n_units_disc = 256
    learning_rate_disc = 1e-4
    dropout_rate = 0.3
    discriminator, _ = build_discriminator(
        input_dim, n_layers_disc, n_units_disc, learning_rate_disc, dropout_rate
    )
    fake = tf.random.normal([1, input_dim])
    decision = discriminator(fake)
    print("Decisão do Discriminador:", decision.numpy())
    discriminator.summary()
