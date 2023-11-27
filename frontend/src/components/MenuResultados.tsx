import { Box, IconButton, Slider, Typography, styled } from "@mui/material";
import StartIcon from "@mui/icons-material/Start";

interface IMenuResultados {
  cambiarMenu: (opcion: number) => void;
}
const MenuResultados: React.FC<IMenuResultados> = ({cambiarMenu}) => {
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
            ¡Aqui está tu recomendación!
        </Typography>
      </Box>
    </Box>
  );
};
export default MenuResultados
