import type { Component } from "solid-js";
import ShoppingList from "./ShoppingList";
import AddItemForm from "./AddItemForm";

const App: Component = () => {
  return (
    <div>
      <h1>My Shopping List App</h1>
      <AddItemForm />
      <ShoppingList />
    </div>
  );
};

export default App;
