MCP Naming Rules & Conventions
==============================

> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

Introduction
------------
In order to guarantee a consistent style and theme across MCP names, the following conventions
SHOULD be adhered to when mapping new things or proposing replacements for existing mappings.

Current mappings MAY deviate from this scheme, but you MUST NOT follow their naming convention when proposing new names. Instead you SHOULD try to fix the old names.

Please refer to this document whenever you do not know how to format or structure a name.

Getting Started
---------------
 - **If you do not know what to name something then *you SHOULD NOT name it*. Let someone else do so.**
 - Names SHOULD reflect intent, *not* solely implementation. Check usages rather than looking only at the definition.
   Also consider overrides and their context.
 - Names SHOULD be concise and memorable, while redundancies SHOULD be avoided. If information can be inferred from context (type, parameters etc.),
   do not include it in the name. This especially applies to fields and methods in a class, where you do not
   need to have the defining class's name in the member's name.
 - Clarification SHOULD preferably reside in the documentation comment, not in verbose names. Conversely, you SHOULD NOT give fields, methods, or method parameters needless comments that only repeat signature and name. Instead, use the documentation
   for non-trivial examples or technical details.

General
-------
 - All names MUST use American English spelling.
 - Acronyms SHOULD generally be written all-lowercase, while normal camel case rules still apply.
   For instance, "identifier" becomes `id` as standalone word or at the beginning of a camel case phrase and
   `Id` when used within a phrase.<br>
   There are various exceptions to this rule which apply only when the word does not start with them:
     - axis-aligned bounding boxes: `AxisAlignedBB` → `AABB`
     - named binary tags → `NBT`
     - red, green, blue (and alpha) color components → `RGB(A)`
     - universally unique identifiers: `UUID` → `UniqueId`

### Examples
 - A class for RGB values SHOULD be called `RGBColor`, not `RgbColour`.
 - A method for adding something to a container SHOULD be called `Container.add`, not `Container.addToContainer`, as that information can be inferred from the class name.

Type Names
----------
 - Type names MUST be named in `UpperCamelCase`.
 - Classes, interfaces etc. MUST follow a suffix-based naming scheme.
   Specifically, this means for any name, `NameType` would be the correct name, where `Type` SHOULD be
   derived from the supertypes.
 - Abstract base classes SHOULD be prefixed with `Abstract`.
 - Interfaces MUST be prefixed with the letter `I`.
 - Enums SHOULD be named directly after the things they are enumerating, in singular form.
   There MUST NOT be an `Enum` prefix/suffix.

### Examples
 - For a new shelf block with an inventory, appropriate names would be `ShelfBlock`, `ShelfTileEntity` and
   `ShelfContainer`.
 - An enumeration for dye colors would be called `DyeColor`.

Field Names
-----------
 - Instance and non-final static fields MUST follow the `camelCase` scheme.
 - `final static` fields (constants) MUST use `CONSTANT_CASE`.
 - `boolean` type fields SHOULD NOT start with an *is* prefix unless there is a convincing reason to do so.
 - Field names MUST NOT use prefixes or suffixes like `the` or `Obj`.

Method Names
------------
 - Methods MUST be named using `camelCase`.
 - Method names SHOULD always start with a verb. Standard conventions for setters and getters apply.
 - Getter-style methods returning a `boolean` SHOULD be named with a phrase that can be used
   in a conditional (if) clause, e.g. some verb or adjective prefixed with some third person verb.
   Common prefixes include `is`, `can`, `has`, and `contains`.
 - 'Event handling' methods SHOULD follow an `on<Noun>` theme where the noun is the event's name
   (with redundancies removed).
 - Methods which store an object's state in a provided container SHOULD be prefixed with `write`.
   This especially applies to methods that write to some NBT tag or the network buffer.
 - Methods which retrieve an object's state from a provided container and apply it to an existing instance
   SHOULD be prefixed with `read`. This especially applies to methods that read from an NBT tag or
   the network buffer.
 - Methods which convert an object's state into some storage format or reconstruct an object from a given
   storage container SHOULD have a `deserialize` or `serialize` prefix accordingly.
   This applies to methods that perform conversions from an object into JSON/NBT and back,
   without manipulating some provided container or existing object instance.

### Examples
 - A boolean getter to check whether a chest was opened in the last few seconds SHOULD be called `wasOpenedRecently`.
 - The method for handling block right clicks SHOULD be called `onActivation` (noun form, no redundancy),
   not `onBlockActivated` (past participle, redundant `Block` infix).

Method Parameter Names
----------------------
 - Parameters MUST follow the `camelCase` scheme.
 - If a name clashes with that of a field or a type name, it SHOULD be suffixed with `In`.
 - Parameters of certain types SHOULD get named according to the following list:
     - `BlockPos` arguments SHOULD be named `pos` when the usage is obvious and `<subject>Pos` when
       there is ambiguity, multiple parameters or the parameter is known to represent something that can not be gleaned from the method name.
     - Parameters of the `IWorldReaderBase` and related types SHOULD be called `worldIn`. You MAY name it differently if the parameter has a known purpose.

### Examples
 - The `World` parameter to a method like `Block.onActivation` SHOULD be called `worldIn`.
 - The two `BlockPos` parameters to a method that calculates the volume of a block cuboid SHOULD be called `startPos` and `endPos`.