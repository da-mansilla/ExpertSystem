import {
  Box,
  Grid,
  IconButton,
  Slider,
  Typography,
  styled,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import RemoveIcon from "@mui/icons-material/Remove";
import { useState } from "react";
import StartIcon from "@mui/icons-material/Start";

interface IMenuComensales {
  cambiarMenu: (opcion: number) => void;
}
const MenuComensales: React.FC<IMenuComensales> = ({ cambiarMenu }) => {
  const [hombresMayores, setHombresMayores] = useState(0);
  const [hombresMenores, setHombresMenores] = useState(0);
  const [mujeresMayores, setMujeresMayores] = useState(0);
  const [mujeresMenores, setMujeresMenores] = useState(0);
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
        <Typography variant="h4" component="h1">
          ¿Cuantos acompañantes vas a tener?
        </Typography>
      </Box>
      <Grid container rowSpacing={9} columnSpacing={1} sx={{ mt: 5 }}>
        <Grid item xs={6}>
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
        <Grid item xs={6}>
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
        <Grid item xs={6}>
          <SumadorComensales
            label="mujeres Mayores"
            valor={mujeresMayores}
            sumar={() => setMujeresMayores(mujeresMayores + 1)}
            restar={() =>
              setMujeresMayores(
                mujeresMayores > 0 ? mujeresMayores - 1 : mujeresMayores,
              )
            }
          />
        </Grid>
        <Grid item xs={6}>
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
      <Box sx ={{width:"100%",display:"flex",flexDirection:"column",justifyContent:"center",alignItems:"center"}}>
        <Typography component="h4" variant="h3" sx={{ mt: 10 }}>
            Siguiente 
        </Typography>
        <IconButton
          onClick={() => cambiarMenu(5)}
          size="large"
          color="success"
          sx={{ width: 150, height: 150 }}
        >
          <StartIcon
            sx={{ width: 150, height: 150, p: 1, borderRadius: 20 }}
          ></StartIcon>
        </IconButton>

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
      }}
    >
      <Typography variant="h4" component="h5">
        {label}
      </Typography>
      <Typography variant="h1" component="h5">
        {valor}
      </Typography>
      <Box>
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
