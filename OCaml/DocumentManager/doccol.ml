open Document;;

(* doccol.ml: Type sand functions for a collection of named documents.
   Tracks a current document and its name along with an association
   list of all docs in the collection.  Preserves uniqueness of names
   in the collection. Makes use of built-in List functions to
   ad/remove/get docs from the association list. *)

(* Type to track a collection of named documents in an association
   list. *)
type 'a doccol = {
  mutable count   : int;                                  (* count of docs in list *)
  mutable curdoc  : 'a Document.document;                 (* current list being edited *)
  mutable curname : string;                               (* name of current list *)
  mutable docs    : (string * 'a Document.document) list; (* association list of names/docs *)
};;

let make name doc =
  {
    count=1;
    curdoc=doc;
    curname=name;
    docs=[(name, doc)]
  }
;;
(* val make : string -> 'a Document.document -> 'a doccol
   Create a doccol. The parameters name and doc become the current
   doc and the only pair in the docs association list. *)

let add doccol name doc =
  match (List.assoc_opt name doccol.docs) with
  | Some x -> false                           (* Preserves uniqueness *)
  | None ->                                   (* Add new element, increment *)
    doccol.count <- doccol.count + 1;
    doccol.docs <- (name, doc) :: doccol.docs; (* Track all current docs, cons tuple to current list *)
    true
;;
(* val add : 'a doccol -> string -> 'a Document.document -> bool
   If there is already a doc with name in doccol, do nothing and
   return false.  Otherwise, add the given doc to doccol with the
   given name, update the count of docs and return true. Uses
   association list functions from the List module. *)

let has doccol name =
  match (List.assoc_opt name doccol.docs) with
  | Some x -> true      (* Uses List.assoc_opt which uses options Some x/None *)
  | None -> false
  ;;
(* val has : 'a doccol -> string -> bool
  Returns true if the named doc is in the doccol and false otherwise. *)

let remove doccol name =
  match (has doccol name) with
  | false -> false
  | true ->
    match doccol.curname with
    | name_string when name_string = name -> false    (* Don't remove if curname = name *)
    | _ ->
      doccol.count <- doccol.count - 1;               (* Okay to remove if curname != name *)
      doccol.docs <- List.remove_assoc name doccol.docs;
      true
;;
(* val remove : 'a doccol -> string -> bool
   If name is equal to curname for the doccol, do nothing and return
   false.  If there is no doc with name in doccol, do nothing and
   return false.  Otherwise, remove the named doc from doccol,
   decrement the count of docs, and return true. Uses association list
   functions from the List module. *)

let switch doccol name =
  match (has doccol name) with
  | false -> false
  | true ->
    doccol.curname <- name;                         (* Put in new curname, curdoc *)
    doccol.curdoc <- List.assoc name doccol.docs;   (* Get document handle *)
    true
;;
(* val switch : 'a doccol -> string -> bool
   Change the current document/name to the named document and return
   true. If the named document does not exist, return false and make
   no changes to doccol. *)

let string_of_doccol doccol =
  let count = Printf.sprintf "%i docs\n" doccol.count in      (* sprintf returns string repr of normal printf *)
  let stringList = List.map (fun (x, y) -> Printf.sprintf "- %s" x) doccol.docs in  (* Make a list if strings uses sprintf *)
  let docString = String.concat "\n" stringList in      (* concantate all elements of the list *)
  count^docString^"\n"    (* return full concatenated string per below output format *)
;;
(* val string_of_col : 'a doccol -> string
   Creates a string representation of doccol showing the count of
   docs and the names of all docs. Each doc is listed on its own
   line. It has the following format:

   4 docs
   - test-dir/heros.txt
   - places.txt
   - stuff.txt
   - default.txt

   Does not define any helper functions. Makes use of higher order
   functions such as List.map and/or List.fold. May also use string
   processing functions such asString.concat and/or Printf.sprintf *)
