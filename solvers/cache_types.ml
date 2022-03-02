[@@@ocaml.warning "-27-30-39"]

type tower_cash_block = {
  x10 : int32;
  w10 : int32;
  h10 : int32;
}

type tower_cash_entry = {
  plan : tower_cash_block list;
  height : float;
  stability : float;
  area : float;
  length : float;
  overpass : float;
  staircase : float;
}

type tower_cash = { entries : tower_cash_entry list } [@@unboxed]

let rec default_tower_cash_block
    ?(x10 : int32 = 0l)
    ?(w10 : int32 = 0l)
    ?(h10 : int32 = 0l)
    () : tower_cash_block =
  { x10; w10; h10 }

let rec default_tower_cash_entry
    ?(plan : tower_cash_block list = [])
    ?(height : float = 0.)
    ?(stability : float = 0.)
    ?(area : float = 0.)
    ?(length : float = 0.)
    ?(overpass : float = 0.)
    ?(staircase : float = 0.)
    () : tower_cash_entry =
  { plan; height; stability; area; length; overpass; staircase }

let rec default_tower_cash ?(entries : tower_cash_entry list = []) () :
    tower_cash =
  { entries }
