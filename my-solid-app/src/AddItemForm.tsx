import { createSignal } from "solid-js";
import axios from "axios";
import styles from "./Style.module.css";

function AddItemForm() {
  // Lokale Zustände für den Namen und die Menge des Artikels
  const [name, setName] = createSignal("");
  const [amount, setAmount] = createSignal(1);

  // Funktion zum Hinzufügen eines Artikels
  const addItem = async () => {
    try {
      await axios.post("http://localhost:8080/api/shopping/create", {
        name: name(),
        amount: amount(),
      });
      alert("Item added successfully");
      setName(""); // Name-Feld leeren
      setAmount(1); // Menge zurücksetzen
    } catch (error) {
      alert("Failed to add item");
    }
  };

  return (
    <div class={styles.container}>
      <h2 class={styles.header}>Add Shopping Item</h2>
      <input
        class={styles.input}
        type="text"
        value={name()}
        onInput={(e) => setName(e.currentTarget.value)}
        placeholder="Item Name"
      />
      <input
        class={styles.input}
        type="number"
        value={amount()}
        onInput={(e) => setAmount(parseInt(e.currentTarget.value))}
        min="1"
        placeholder="Amount"
      />
      <button class={styles.button} onClick={addItem}>Add Item</button>
    </div>
  );
}

export default AddItemForm;
