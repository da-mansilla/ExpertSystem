import { Paper } from "@mui/material";
import { useState } from "react";
import MenuPrincipal from "./components/MenuPrincipal";
import MenuPlatillo from "./components/MenuPlatillo";
import MenuDinero from "./components/MenuDinero";
import MenuComensales from "./components/MenuComensales";
import MenuResultados from "./components/MenuResultados";

function App() {
  const [menu, setMenu] = useState(1);
  const [platilloSeleccionado, setPlatilloSeleccionado] = useState("");
  const cambiarMenu = (opcion: number) => {
    setMenu(opcion);
    console.log(opcion);
  };
  const selectPlatillo = (platillo: string) => {
    console.log(platillo);
    setPlatilloSeleccionado(platillo);
    setMenu(3);
  };
  return (
    <Paper
      elevation={12}
      sx={{
        position: "absolute",
        width: "55%",
        height: "75%",
        // backgroundColor: "#E5E7EB",
        left: "50%",
        top: "50%",
        p: 10,
        transform: "translate(-50%, -50%)",
        borderRadius: 4,
      }}
    >
      {menu === 1 && <MenuPrincipal cambiarMenu={cambiarMenu} />}
      {menu === 2 && (
        <MenuPlatillo
          cambiarMenu={cambiarMenu}
          selectPlatillo={selectPlatillo}
        />
      )}
      {menu === 3 && <MenuDinero cambiarMenu={cambiarMenu} />}
      {menu === 4 && <MenuComensales cambiarMenu={cambiarMenu} />}
      {menu === 5 && <MenuResultados cambiarMenu={cambiarMenu} />}
    </Paper>
  );
}

export default App;
