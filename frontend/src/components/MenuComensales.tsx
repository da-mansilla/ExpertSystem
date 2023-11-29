import { Box, Button, Grid, IconButton, Typography } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import RemoveIcon from "@mui/icons-material/Remove";
import { useState } from "react";
import { Comensales } from "../App";

interface IMenuComensales {
  changeComensales: (comensales: Comensales) => void;
}
const MenuComensales: React.FC<IMenuComensales> = ({
  changeComensales,
}) => {
  const [hombresMayores, setHombresMayores] = useState(0);
  const [hombresMenores, setHombresMenores] = useState(0);
  const [mujeresMayores, setMujeresMayores] = useState(0);
  const [mujeresMenores, setMujeresMenores] = useState(0);
  const handleOnClickButton = () => {
    const newComensales = {
      hombresMayores: hombresMayores,
      hombresMenores: hombresMenores,
      mujeresMayores: mujeresMayores,
      mujeresMenores: mujeresMenores,
    };
    changeComensales(newComensales);
    // getResults()

    // cambiarMenu(5)
  };
  return (
    <Box>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Box
          sx={{
            py: 2,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <Typography
            component="h2"
            variant="h4"
            sx={{ mt: 0, color: "gray", fontWeight: "bold" }}
          >
            ¿Cuantos van a comer?
          </Typography>
        </Box>
      </Box>
      <Grid container rowSpacing={0} columnSpacing={1} sx={{ mt: 0, pt: 0 }}>
        <Grid item xs={6} sx={{ pt: 0 }}>
          <SumadorComensales
            label="Hombres Mayores"
            valor={hombresMayores}
            sumar={() => setHombresMayores(hombresMayores + 1)}
            restar={() =>
              setHombresMayores(
                hombresMayores > 0 ? hombresMayores - 1 : hombresMayores,
              )
            }
          />
        </Grid>
        <Grid item xs={6} sx={{ p: 0 }}>
          <SumadorComensales
            label="Hombres Menores"
            valor={hombresMenores}
            sumar={() => setHombresMenores(hombresMenores + 1)}
            restar={() =>
              setHombresMenores(
                hombresMenores > 0 ? hombresMenores - 1 : hombresMenores,
              )
            }
          />
        </Grid>
        <Grid item xs={6} sx={{ p: 0 }}>
          <SumadorComensales
            label="Mujeres Mayores"
            valor={mujeresMayores}
            sumar={() => setMujeresMayores(mujeresMayores + 1)}
            restar={() =>
              setMujeresMayores(
                mujeresMayores > 0 ? mujeresMayores - 1 : mujeresMayores,
              )
            }
          />
        </Grid>
        <Grid item xs={6} sx={{ p: 0 }}>
          <SumadorComensales
            label="Mujeres Menores"
            valor={mujeresMenores}
            sumar={() => setMujeresMenores(mujeresMenores + 1)}
            restar={() =>
              setMujeresMenores(
                mujeresMenores > 0 ? mujeresMenores - 1 : mujeresMenores,
              )
            }
          />
        </Grid>
      </Grid>
      <Box
        sx={{
          width: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          mt: 3,
        }}
      >
        <Button
        onClick={() => handleOnClickButton()}
          sx={{
            width: "50%",
            backgroundColor: "#FF3C53",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            borderRadius: 20,
            ":hover":{backgroundColor:"#FF3F43"}
          }}
        >
          <Typography
            component="h4"
            variant="h4"
            sx={{ py: 2, color: "white", fontWeight: "bold" }}
          >
            Terminar
          </Typography>
        </Button>
      </Box>
    </Box>
  );
};

interface ISumadorComensales {
  label: string;
  valor: number;
  sumar: () => void;
  restar: () => void;
}
const SumadorComensales: React.FC<ISumadorComensales> = ({
  label,
  valor,
  sumar,
  restar,
}) => {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        p: 0,
      }}
    >
      <Typography variant="h5" component="p">
        {label}
      </Typography>
      <Typography variant="h1" component="p">
        {valor}
      </Typography>
      <Box sx={{ p: 0 }}>
        <IconButton onClick={restar}>
          <RemoveIcon color="error" sx={{ width: 60, height: 60 }} />
        </IconButton>
        <IconButton onClick={sumar}>
          <AddIcon color="success" sx={{ width: 60, height: 60 }} />
        </IconButton>
      </Box>
    </Box>
  );
};

export default MenuComensales;
