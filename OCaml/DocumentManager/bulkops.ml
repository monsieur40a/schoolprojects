open Util;;
open Sortedlist;;
open Document;;
open Doccol;;


(* bulkops.ml: Implement bulk operations on Doccol's of string list
   Documents that are useful for multimanager.  Since the functions in
   this module require access to fields and types of other modules, start
   the file by opening those two modules:

   open Document;;
   open Doccol;;
*)

let showall doccol =
  let helper (name,doc) =       (* Processes docs tuple per desired format *)
    Printf.printf "--List %s--\n" name;
    let docStrList = doc.current in
    Sortedlist.print docStrList;  (* Uses recursive print function in Sortedlist for str list argument *)
  in
  List.iter helper doccol.docs;   (* (helper -> unit) -> string list Doccol.doccol -> unit) *)
  Printf.printf "\n"; (* Needed for proper spacing *)
;;

(* let showall doccol =
  let helper (name,doc) =

  in
  ...
; *)
(* val showall : string list Doccol.doccol -> unit
   Prints all documents in doccol to the screen. For each list,
   prints the list name first and then each element of the list using
   Sortedlist functions. Uses higher-order functions to iterate over
   the doclist.

   EXAMPLE:
   --List test-data/heros.txt--
   Asami
   Bolin
   Bumi
   Jinora
   Korra
   Kya
   Mako
   Tenzin

   --List test-data/villains.txt--
   Amon
   Hiroshi
   Kuvira
   Ming-Hua
   P-li
   Unalaq
   Zaheer

   --List default.txt--
   Korra
   Meelo
   Pema
*)

let saveall doccol =
  let helper (name,doc) =
    let docStrList = doc.current in
    Util.strlist_to_file docStrList name;  (* Save document's current list state to associated name *)
  in
  List.iter helper doccol.docs;  (* (helper -> unit) -> string list Doccol.doccol -> unit) *)
;;
(* val saveall : string list Doccol.doccol -> unit
   Saves all documents in doccol. Makes use of Util functions to do
   I/O. Makes use of higher-order functions to write each list to
   associated file name. *)

let addall doccol elem =
  let helper (name,doc) =
    let docStrList = doc.current in       (* Get current string list state *)
    let newdocStrList = Sortedlist.insert docStrList elem in  (* Insert elem into list, return sorted string list *)
    Document.set doc newdocStrList;   (* update current string list state *)
  in
  List.iter helper doccol.docs; (* (helper -> unit) -> string list Doccol.doccol -> unit) *)
;;
(* val addall : 'a list Doccol.doccol -> 'a -> unit
   Adds the given element to all docs in doccol. Makes use of
   higher-order functions and Sortedlist functions to modify each
   list. Each doc/list can individually undo the addition. *)

let copyall doccol elem =
  let helper (name,doc) =


| "copyto" ->
  begin
  let new_name = tokens.(1) in
  let new_doc =
    Document.make global.curdoc.current in
  let added =
    Doccol.add global new_name new_doc in
  if added then
    printf...
  end


let mergeall doccol =
  let helper currList (name, doc) =   (* currList is current merged list in fold_left processing of list *)
    Sortedlist.merge currList doc.current (* merges currList and current docs string list into a new sorted string list *)
  in
  List.fold_left helper [] doccol.docs;  (* (helper -> newMergedList) -> currListState -> doccol.docs list -> allListsMerged*)
;;
(* val mergeall : 'a list Doccol.doccol -> 'a list
   Merges all lists in doccol.docs into a single list and returns
   it. Uses higher-order functions and Sortedlist functions to perform
   the merge. *)
