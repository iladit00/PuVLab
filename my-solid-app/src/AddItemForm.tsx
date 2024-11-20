import { createSignal } from "solid-js";
import axios from "axios";

function AddItemForm() {
  // Lokale Zustände für den Namen und die Menge des Artikels
  const [name, setName] = createSignal("");
  const [amount, setAmount] = createSignal(1);

  // Funktion zum Hinzufügen eines Artikels
  const addItem = async () => {
    try {
      await axios.post("http://localhost:8000/api/shopping/create", {
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
    <div>
      <h2>Add Shopping Item</h2>
      <input
        type="text"
        value={name()}
        onInput={(e) => setName(e.currentTarget.value)}
        placeholder="Item Name"
      />
      <input
        type="number"
        value={amount()}
        onInput={(e) => setAmount(parseInt(e.currentTarget.value))}
        min="1"
        placeholder="Amount"
      />
      <button onClick={addItem}>Add Item</button>
    </div>
  );
}

export default AddItemForm;
