# catch_ohl Kurzuebersicht

- `dict_tree_examples.py`: `inorder`, `preorder`, `postorder`, `levelorder`, `count_values`, `inorder_list`, `preorder_list`, `postorder_list`, `levelorder_list` - durchlaeuft verschachtelte Dictionary-Baeume wie in `simpleBinaryTree`, einmal als String und einmal als Liste.
- `getters_setters.py`: `ExamNode` Getter/Setter, `connect_left`, `connect_right`, `is_left_child` - zeigt Klassenattribute, Properties und Parent/Child-Links in beide Richtungen.
- `json_load_dump.py`: `nil`, `new_node`, `insert`, `preorder_items`, `to_dict`, `from_dict`, `dump`, `load`, `inorder_keys` - speichert und laedt einen flachen JSON-Key/Value-Baum, wahlweise mit Datei oder direkt als `dict`.
- `rb_access_methods.py`: `RBTree.max`, `min`, `find_node`, `find`, `between`, `count_between`, `visit_post_order`, `visit_level_order` - zeigt klausurnahe Zugriffsmethoden auf RBTree-Knoten mit NIL-Knoten.
- `rb_delete_examples.py`: `search`, `minimum`, `successor`, `transplant`, `delete`, `delete_if_exists`, `fix_delete`, Rotationen - zeigt den RBTree-Delete-Ablauf, Nachfolger und den Sonderfall fehlender Key.
- `rb_insert_examples.py`: `insert`, `insert_or_replace`, `insert_many`, `find_node`, `fix_insert`, `left_rotate`, `right_rotate`, `inorder` - zeigt RBTree-Insert, Reparatur nach dem Einfuegen und einfache Duplikat-/Mehrfachvarianten.
- `rb_validation.py`: `count_color`, `count_nil`, `validate_bst_order`, `validate_parent_links`, `black_height`, `no_red_red`, `validate_rb_tree` - prueft einfache RBTree-Regeln, NIL-Knoten und Parent-Links.
- `search_min_max_between.py`: `find`, `find_or_default`, `min_key`, `max_key`, `between`, `between_as_string`, `insert_bst` - uebt Suche, Minimum, Maximum, Bereichsabfrage und andere Rueckgabeformen.
- `simple_node.py`: `Node`, `nil`, `leaf`, `has_nil_children`, `set_left`, `set_right` - zeigt RED/BLACK/NIL-Grundlagen eines Knotens und einfache Kind/Parent-Verbindungen.
- `traversals.py`: `inorder`, `preorder`, `postorder`, `levelorder`, `levelorder_with_level`, `visit_in_order`, `visit_post_order`, `visit_level_order` - uebt die wichtigsten Traversal-Reihenfolgen, Callback-Varianten und Ebeneninformationen.
