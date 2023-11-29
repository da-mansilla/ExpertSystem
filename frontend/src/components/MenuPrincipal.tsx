import { Box, IconButton, Typography } from "@mui/material";
import StartIcon from "@mui/icons-material/Start";

export interface IMenuPrincipal {
  cambiarMenu: (opcion: number) => void;
}
const MenuPrincipal: React.FC<IMenuPrincipal> = ({ cambiarMenu }) => {
  return (
    <Box>
      <Box
        sx={{
          py: 3,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Typography
          component="h2"
          variant="h4"
          sx={{ mt: 2, color: "gray", fontWeight: "bold" }}
        >
          ! Recibe una recomendación personalizada !
        </Typography>
      </Box>
      <Box
        sx={{
          mt: 10,
          display: "flex",
          flexDirection: "column",
          justifyContent: "start",
          alignItems: "center",
          height: "65%",
        }}
      >
        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            justifyContent: "start",
            alignItems: "center",
            backgroundColor: "white",
            border: 1,
            borderColor: "#FF3C53",
            width: "20%",
            p: 10,
            borderRadius: 100,
          }}
        >
          <Typography
            component="h3"
            variant="h3"
            sx={{ color: "#FF3C53", fontWeight: "bold" }}
          >
            Comenzar
          </Typography>
          <IconButton
            onClick={() => cambiarMenu(2)}
            size="large"
            sx={{ width: 150, height: 150, color: "#FF3C53" }}
          >
            <StartIcon
              sx={{ width: 150, height: 150, p: 0, borderRadius: 20 }}
            ></StartIcon>
          </IconButton>
        </Box>
      </Box>
    </Box>
  );
};
export default MenuPrincipal;
