import tensorflow as tf # pragma: no cover
from keras import layers # pragma: no cover


## Removing from tests for now since I am not sure I'll keep using discriminatos and generator
class Generator(tf.keras.Model):  # pragma: no cover
    def __init__(self, noise_dim, output_dim, n_layers, n_units):
        super(Generator, self).__init__()
        self.model = tf.keras.Sequential()
        for i in range(n_layers):
            self.model.add(
                layers.Dense(
                    n_units if i > 0 else 128, input_dim=noise_dim if i == 0 else None
                )
            )
            self.model.add(layers.LeakyReLU(alpha=0.2))
            self.model.add(layers.BatchNormalization())

    def call(self, inputs):
        return self.model(inputs)


def build_generator(noise_dim, output_dim, n_layers, n_units, learning_rate): # pragma: no cover
    generator = Generator(noise_dim, output_dim, n_layers, n_units)
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    return generator, optimizer


## Below code only makes sense when running local so will not be considered for teste
if __name__ == "__main__":  # pragma: no cover
    # Exemplo de uso para verificar a arquitetura
    noise_dim = 100
    output_dim = 11  # Número de features nos seus dados
    n_layers_gen = 3
    n_units_gen = 256
    learning_rate_gen = 1e-4
    generator, _ = build_generator(
        noise_dim, output_dim, n_layers_gen, n_units_gen, learning_rate_gen
    )
    noise = tf.random.normal([1, noise_dim])
    generated_output = generator(noise)
    print("Output do Gerador:", generated_output.shape)
    generator.summary()
