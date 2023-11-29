import { Box, IconButton, Slider, Typography, styled } from "@mui/material";
import StartIcon from "@mui/icons-material/Start";

interface IMenuDinero {
  cambiarMenu: (opcion: number) => void;
  dinero: number
  changeDinero: (dinero:number) => void
}
const MenuDinero: React.FC<IMenuDinero> = ({cambiarMenu,dinero,changeDinero}) => {
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
         ¿Cúal es tu Presupesto? 
        </Typography>
      </Box>
      </Box>
      <Box sx={{mt:15,mx:10}}>
        <PrettoSlider
          value={dinero}
          step={100}
          onChange={(e:any) => changeDinero(e.target.value)}
          valueLabelDisplay="on"
          valueLabelFormat={(value) => "$ "+value}
          aria-label="pretto slider"
          defaultValue={20}
          min={1000}
          max={20000}
        />
      </Box>
      <Box
        sx={{
          mt: 3,
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
            Siguiente 
          </Typography>
          <IconButton
            onClick={() => cambiarMenu(4)}
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

const PrettoSlider = styled(Slider)({
  color: "#52af77",
  height: 8,
  "& .MuiSlider-track": {
    border: "none",
  },
  "& .MuiSlider-thumb": {
    height: 44,
    width: 44,
    backgroundColor: "#fff",
    border: "2px solid currentColor",
    "&:focus, &:hover, &.Mui-active, &.Mui-focusVisible": {
      boxShadow: "inherit",
    },
    "&:before": {
      display: "none",
    },
  },
  "& .MuiSlider-valueLabel": {
    lineHeight: 1.2,
    fontSize: 21,
    background: "unset",
    padding: 25,
    width: 42,
    height: 42,
    borderRadius: "50% 50% 50% 0",
    backgroundColor: "#52af77",
    transformOrigin: "bottom left",
    transform: "translate(50%, -100%) rotate(-45deg) scale(0)",
    "&:before": { display: "none" },
    "&.MuiSlider-valueLabelOpen": {
      transform: "translate(50%, -100%) rotate(-45deg) scale(1)",
    },
    "& > *": {
      transform: "rotate(45deg)",
    },
  },
});

export default MenuDinero;
