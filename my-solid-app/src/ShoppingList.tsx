import { createSignal, createResource } from "solid-js";
import axios from "axios";

// Definition der Struktur eines Shopping-Items
interface ShoppingItem {
  name: string;
  amount: number;
}

function ShoppingList() {
  // createResource, um die Shopping-Items aus der API abzurufen
  const [items, { refetch }] = createResource<ShoppingItem[]>(async () => {
    try {
      const response = await axios.get("http://localhost:8000/api/shopping/");
      return response.data;
    } catch (error) {
      console.error("Error fetching shopping items:", error);
      return []; // Rückgabe einer leeren Liste bei Fehler
    }
  });

  // Funktion zum Aktualisieren der Menge eines Artikels
  const updateAmount = async (name: string, newAmount: number) => {
    try {
      await axios.put(`http://localhost:8000/api/shopping/${name}/update`, {
        amount: newAmount,
      });
      alert(`Updated ${name} successfully`);
      refetch(); // Liste nach dem Update erneut abrufen
    } catch (error) {
      alert("Failed to update item");
      console.error("Error updating item:", error);
    }
  };

  // Funktion zum Löschen eines Artikels
  const deleteItem = async (name: string) => {
    try {
      await axios.delete(`http://localhost:8000/api/shopping/${name}/delete`);
      alert(`Deleted ${name} successfully`);
      refetch(); // Liste nach dem Löschen erneut abrufen
    } catch (error) {
      alert("Failed to delete item");
      console.error("Error deleting item:", error);
    }
  };

  return (
    <div>
      <h2>Shopping Items</h2>
      <button onClick={() => refetch()}>Refresh List</button>
      <ul>
        {items.loading && <li>Loading...</li>}
        {items()?.map((item) => (
          <li>
            {item.name} - {item.amount}
            <input
              type="number"
              min="1"
              value={item.amount}
              onInput={(e) => updateAmount(item.name, parseInt(e.currentTarget.value))}
            />
            <button onClick={() => deleteItem(item.name)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ShoppingList;
