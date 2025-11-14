import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)
def build_model(hidden_units=128, learning_rate=0.001):
    model = models.Sequential([
        layers.Dense(hidden_units, activation='relu', input_shape=(784,)),
        layers.Dense(hidden_units // 2, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    optimizer = optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model
hidden_units_list = [64, 128, 256]
learning_rates = [0.01, 0.001]
batch_sizes = [64, 128]
best_acc = 0
best_config = None
for hidden_units in hidden_units_list:
    for lr in learning_rates:
        for batch in batch_sizes:
            print(f"\nTraining model: hidden_units={hidden_units}, lr={lr}, batch={batch}")
            model = build_model(hidden_units, lr)
            history = model.fit(x_train, y_train, epochs=3, batch_size=batch, validation_split=0.1, verbose=0)
            val_acc = history.history['val_accuracy'][-1]
            print(f"Validation Accuracy: {val_acc:.4f}")
            if val_acc > best_acc:
                best_acc = val_acc
                best_config = (hidden_units, lr, batch)
print(f"\nBest configuration -> Hidden Units: {best_config[0]}, Learning Rate: {best_config[1]}, Batch Size: {best_config[2]}")
final_model = build_model(best_config[0], best_config[1])
final_model.fit(x_train, y_train, epochs=5, batch_size=best_config[2], validation_split=0.1, verbose=1)
test_loss, test_acc = final_model.evaluate(x_test, y_test)
print(f"Test Accuracy (Best Model): {test_acc:.4f}")
predictions = final_model.predict(x_test[:10])
predicted_labels = np.argmax(predictions, axis=1)
plt.figure(figsize=(8, 4))
for i in range(2):
    plt.suptitle("Name : Aryan Rana | Roll No. : 1323223", fontsize=8)
    plt.subplot(1, 2, i + 1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Pred: {predicted_labels[i]}, True: {y_test[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()
